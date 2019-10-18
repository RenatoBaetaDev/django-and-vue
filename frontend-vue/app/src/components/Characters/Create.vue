<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on }">
        <v-card-text>
          <v-fab-transition>
            <v-btn primary v-on="on" dark relative fixed bottom right fab>
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-fab-transition>
        </v-card-text>
      </template>

      <v-card>
        <v-card-title>
          <span class="headline">Adicionar Personagem</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field 
                  v-model="character.name" 
                  label="Nome*" 
                  hint="Nome do Personagem" 
                  required
                ></v-text-field>
              </v-col>
              
              <v-col cols="12">
                <v-text-field
                  v-model="character.book"
                  label="Livro*"
                  hint="Livro do Personagem"
                  required
                ></v-text-field>
              </v-col>

              <v-col class="d-flex" cols="12">
                <v-select
                  v-model="character.gender"
                  item-text="gender"
                  item-value="value"
                  :items="items"
                  label="Gênero*"
                  hint="Gênero do Personagem"
                  required
                  dense
                ></v-select>
              </v-col>              

              <v-col cols="12">
                <v-text-field v-model="character.description" label="Descrição*" type="text" required></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-file-input
                  v-model="character.picture"
                  label="Imagem"
                  hint="Imagem do Personagem"
                  prepend-icon="mdi-camera"      
                  accept="image/*"          
                >
                </v-file-input>
              </v-col>
            </v-row>
          </v-container>
          <small>*informações obrigatórias</small>
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1"></div>
          <v-btn color="blue darken-1" text @click="dialog = false">Fechar</v-btn>
          <v-btn color="blue darken-1" text @click="add()">Salvar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
import axios from "axios"   
export default {
  name: "CreateCharacter",
  data() {
    return {
      dialog: false,
      character: {},
      items: [
        {
          value: 1,
          gender:'Masculino',
        },
        { 
          value: 2,
          gender:'Feminino',
        },
        {
          value: 3,
          gender:'Outro',
        }
      ]
    };
  },
  methods: {
    add() {      
      this.character.picture = this.character.picture.name
      console.log(this.character)
      axios
        .post("http://localhost:8000/api/characters/add/",
          this.character, 
          {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          }
        )
        .then(response => {
          this.dialog = false
          this.$emit('updateCharacters')
          this.log.console(response)
        });
    }
  }
};
</script>
