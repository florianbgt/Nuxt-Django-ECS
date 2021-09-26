<template>
  <b-form @submit.prevent="editRecipe">
    <h1>Edit recipe</h1>
    <b-form-group label="Name:">
      <b-form-input
        v-model="name"
        placeholder="Enter a name ..."
        trim
        required
      ></b-form-input>
    </b-form-group>
    <b-form-group label="Photo:">
      <b-form-file v-model="image" accept="image/*"></b-form-file>
    </b-form-group>
    <b-form-group label="instruction:">
      <b-form-textarea
        id="textarea"
        v-model="instruction"
        placeholder="Enter instruction..."
        rows="3"
        max-rows="20"
        trim
        required
      ></b-form-textarea>
    </b-form-group>
    <b-row class="justify-content-center">
      <b-col cols="6" sm="4" md="3" lg="2">
        <b-button :to="`/recipes/${recipeId}`" block>Cancel</b-button>
      </b-col>
      <b-col cols="6" sm="4" md="3" lg="2">
        <b-button type="submit" block variant="warning">Edit</b-button>
      </b-col>
    </b-row>
  </b-form>
</template>

<script>
export default {
  async asyncData({ params, store, $auth, error }) {
    await store.dispatch("recipes/getRecipes");
    const recipe = store.getters["recipes/recipes"].find(
      (recipe) => recipe.id === parseInt(params.recipe)
    );
    if (!recipe) {
      error({ statusCode: 404, message: "Page not found" });
      return
    }
    if (recipe.user.id !== $auth.user.id ) {
      error({ statusCode: 403, message: "You do not have access to this resource" });
      return
    }
    const name = recipe.name;
    const instruction = recipe.instruction;
    return {name, instruction};
  },
  data() {
    return {
      name: null,
      image: null,
      instruction: null,
    };
  },
  computed: {
    recipeId() {
      return parseInt(
        this.$route.path.split("/")[this.$route.path.split("/").length - 2]
      );
    },
    recipe() {
      return this.$store.getters["recipes/recipes"].find(
        (recipe) => recipe.id === this.recipeId
      );
    },
  },
  methods: {
    async fetchRecipes() {
      await this.$store.dispatch("recipes/getRecipes");
    },
    async editRecipe() {
      try {
        await this.$store.dispatch("recipes/editRecipe", {
          id: this.recipeId,
          name: this.name,
          image: this.image,
          instruction: this.instruction,
        });
        this.$router.push(`/recipes/${this.recipeId}`);
      } catch (err) {
        console.log(err);
        this.$bvToast.toast("An error occured while editing your recipe", {
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