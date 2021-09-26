<template>
  <b-form @submit.prevent="addRecipe">
    <h1>Add a new recipe</h1>
    <b-form-group label="Name:">
      <b-form-input v-model="name" trim required></b-form-input>
    </b-form-group>
    <b-form-group label="Photo:">
      <b-form-file v-model="image" accept="image/*" required></b-form-file>
    </b-form-group>
    <b-form-group label="Instructions:">
      <b-form-textarea
        id="textarea"
        v-model="instruction"
        placeholder="Enter instructions..."
        rows="3"
        max-rows="20"
        trim
        required
      ></b-form-textarea>
    </b-form-group>
    <b-row class="justify-content-center">
      <b-col cols="6" sm="4" md="3" lg="2">
        <b-button to="/recipes" block>Cancel</b-button>
      </b-col>
      <b-col cols="6" sm="4" md="3" lg="2">
        <b-button type="submit" block variant="success">Add</b-button>
      </b-col>
    </b-row>
  </b-form>
</template>

<script>
export default {
  data() {
    return {
      name: null,
      image: null,
      instruction: null,
    };
  },
  methods: {
    async addRecipe() {
      try {
        const recipe = await this.$store.dispatch("recipes/addRecipe", {
          name: this.name,
          image: this.image,
          instruction: this.instruction,
        });
        this.$router.push(`/recipes/${recipe.id}`);
      } catch (err) {
        console.log(err);
        this.$bvToast.toast("An error occured while adding your recipe", {
          title: "Error",
          autoHideDelay: 5000,
          appendToast: false,
          toaster: "b-toaster-top-center",
          solid: true,
          variant: "danger",
        });
      }
    },
  },
};
</script>