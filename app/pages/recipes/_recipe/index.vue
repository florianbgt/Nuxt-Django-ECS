<template>
  <div>
    <b-button to="/recipes" block class="d-sm-none mb-2"
      >view all recipes</b-button
    >
    <b-img
      thumbnail
      rounded
      :src="recipe.image"
      :alt="`image-${recipe.name}`"
      style="width: 100%; height: 250px; object-fit: cover"
    />
    <h1>{{ recipe.name }}</h1>
    <b-row v-if="recipe.user.id === $auth.user.id">
      <b-col cols="6" sm="4" md="3" lg="2">
        <b-button :to="`/recipes/${recipeId}/edit`" block variant="warning"
          >Edit</b-button
        >
      </b-col>
      <b-col cols="6" sm="4" md="3" lg="2">
        <b-button :to="`/recipes/${recipeId}/delete`" block variant="danger"
          >Delete</b-button
        >
      </b-col>
    </b-row>
    <h2>
      <small
        >Created
        {{
          new Date(recipe.created_at).toLocaleDateString("en", {
            year: "numeric",
            month: "long",
            day: "numeric",
          })
        }}</small
      >
    </h2>
    <h2>
      <small
        >Updated
        {{
          new Date(recipe.updated_at).toLocaleDateString("en", {
            year: "numeric",
            month: "long",
            day: "numeric",
          })
        }}</small
      >
    </h2>
    <p>
      <big
        ><strong>By {{ recipe.user.email }}</strong></big
      >
    </p>
    <p style="white-space: pre-line">
      {{ recipe.instruction }}
    </p>
  </div>
</template>

<script>
export default {
  async asyncData({ params, store, error }) {
    await store.dispatch("recipes/getRecipes");
    const recipe = store.getters["recipes/recipes"].find(
      (recipe) => recipe.id === parseInt(params.recipe)
    );
    if (!recipe) {
      error({ statusCode: 404, message: "Page not found" });
      return
    }
    return recipe;
  },
  computed: {
    recipeId() {
      return parseInt(
        this.$route.path.split("/")[this.$route.path.split("/").length - 1]
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
  },
};
</script>