<template>
  <b-form @submit.prevent="deleteRecipe">
    <p class="text-danger text-center">
      <big
        ><strong
          >You are about to delete this recipe, are you sure?</strong
        ></big
      >
    </p>
    <b-row class="justify-content-center">
      <b-col cols="6" sm="4" md="3" lg="2">
        <b-button :to="`/recipes/${recipeId}`" block>Cancel</b-button>
      </b-col>
      <b-col cols="6" sm="4" md="3" lg="2">
        <b-button type="submit" block variant="danger">Delete</b-button>
      </b-col>
    </b-row>
  </b-form>
</template>

<script>
export default {
  async fetch() {
    if (
      !this.$store.getters["recipes/recipes"].find(
        (recipe) => recipe.id === this.recipeId
      )
    ) {
      await this.fetchRecipes();
    }
  },
  computed: {
    recipeId() {
      return parseInt(
        this.$route.path.split("/")[this.$route.path.split("/").length - 2]
      );
    },
  },
  methods: {
    async fetchRecipes() {
      await this.$store.dispatch("recipes/getRecipes");
      if (!this.recipe) {
        this.$nuxt.error({
          statusCode: 404,
          message: `Recipe id ${this.recipeId} does not exists`,
        });
      }
    },
    async deleteRecipe() {
      try {
        await this.$store.dispatch("recipes/deleteRecipe", this.recipeId);
        this.$router.push("/recipes");
      } catch (err) {
        console.log(err);
        this.$bvToast.toast("An error occured while deleting your recipe", {
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