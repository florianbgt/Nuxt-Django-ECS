<template>
  <div>
    <p>
      <big><strong>Browse awesome recipes!</strong></big>
    </p>
    <b-row>
      <b-col cols="12" sm="6" md="4" lg="3" xl="2"
        ><b-button to="/recipes/add" block class="mb-2">Add a new recipe</b-button>
      </b-col>
    </b-row>
    <b-row>
      <b-col
        v-for="recipe in recipes"
        :key="recipe.id"
        sm="6"
        lg="4"
        class="mb-4"
      >
        <NuxtLink :to="`/recipes/${recipe.id}`" class="text-dark">
          <b-card :to="`/${recipe.id}`" class="h-100">
            <b-img
              thumbnail
              rounded
              :src="recipe.image"
              :alt="`image-${recipe.name}`"
              style="width: 100%; height: 150px; object-fit: cover"
            />
            <h1>{{ recipe.name }}</h1>
          </b-card>
        </NuxtLink>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  async fetch() {
    await this.fetchRecipes();
  },
  computed: {
    recipes() {
      return this.$store.getters["recipes/recipes"];
    },
  },
  methods: {
    async fetchRecipes() {
      await this.$store.dispatch("recipes/getRecipes");
    },
  },
};
</script>