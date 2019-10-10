<template>
  <v-container>
      <div v-for="character in characters" v-bind:key="character.id">
        <p>{{character.name}}</p>
        <p>{{character.author}}</p>
        <p>{{character.description}}</p>
        
        <v-btn class="ma-2" text icon color="red lighten-2">
          <v-icon class="delete" @click="deleteCharacter(character)"></v-icon>
        </v-btn>
        <v-btn class="ma-2" text icon color="green">
          <v-icon class="edit" @click="editCharacter(character)"></v-icon>
        </v-btn>
        <v-divider></v-divider>
      </div>
      <CreateCharacters @updateCharacters="all"></CreateCharacters>
  </v-container>
</template>


<script>
import axios from "axios";
import router from "@/router/"
import CreateCharacters from "./Create";

export default {
  name: "ListCharacters",
  data() {
    return {
      characters: [],
    };
  },
  components: {
    CreateCharacters: CreateCharacters,
  },
  created() {
    this.all();
  },
  methods: {
    all() {
      axios
        .request({
          baseURL: "http://localhost:8000",
          method: "get",
          url: "/api/characters/"
        })
        .then(response => {
          this.characters = response.data
          console.log(response)
        });
    },
    deleteCharacter(character) {
      if (confirm("Excluir " + character.name)) {
        axios
          .delete(`http://localhost:8000/api/characters/${character.id}`, {
            headers: {
              Authorization: `Token ${this.$session.get("token")}`
            }
          })
          .then(response => {
            this.all()
            console.log(response)
          });
      }
    },
    editCharacter(character) {
      router.push(`/characters/edit/${character.id}`)
    }
  }
};
</script>