import Vue from "vue";

export const state = () => ({
  recipes: [],
});

export const mutations = {
  setRecipes(state, payload) {
    state.recipes = payload;
  },

  editRecipe(state, payload) {
    const index = state.recipes.findIndex((recipe) => recipe.id === payload.id);
    Vue.set(state.recipes, index, payload);
  },

  addRecipe(state, payload) {
    state.recipes.push(payload);
  },

  addRecipe(state, payload) {
    state.recipes.push(payload);
  },

  deleteRecipe(state, payload) {
    const index = state.recipes.findIndex((recipe) => recipe.id === payload);
    state.recipes.splice(index, 1);
  },
};

export const actions = {
  async getRecipes(context) {
    const response = await this.$axios.$get("recipes/");
    if (process.server) {
      response.forEach((recipe) => {
        recipe.image = recipe.image.replace(
          this.$config.axios.baseURL,
          this.$config.axios.browserBaseURL
        );
      });
    }
    context.commit("setRecipes", response);
  },

  async addRecipe(context, payload) {
    let formData = new FormData();
    formData.append("name", payload.name);
    if (!!payload.image) {
      formData.append("image", payload.image);
    }
    formData.append("instruction", payload.instruction);
    const response = await this.$axios.$post("recipes/", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    context.commit("addRecipe", response);
    return response;
  },

  async editRecipe(context, payload) {
    let formData = new FormData();
    formData.append("name", payload.name);
    if (!!payload.image) {
      formData.append("image", payload.image);
    }
    formData.append("instruction", payload.instruction);
    const response = await this.$axios.$patch(
      `recipes/${payload.id}/`,
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );
    context.commit("editRecipe", response);
    return response;
  },

  async deleteRecipe(context, payload) {
    const response = await this.$axios.$delete(`recipes/${payload}/`);
    context.commit("deleteRecipe", payload);
    return response;
  },
};

export const getters = {
  recipes(state) {
    return state.recipes;
  },
};