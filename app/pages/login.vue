<template>
  <div class="w-100" style="max-width: 500px">
    <b-card title="Log In" class="bg-secondary text-light">
      <b-form @submit.prevent="login">
        <b-form-group id="email" label="Email" label-for="input-email">
          <b-form-input
            v-model="email"
            id="input-email"
            type="email"
            placeholder="Enter Email"
            autocomplete="username"
            required
            :disabled="loading"
          />
        </b-form-group>
        <b-form-group id="password" label="Password" label-for="input-password">
          <b-form-input
            v-model="password"
            id="input-password"
            type="password"
            placeholder="Enter Password"
            autocomplete="current-password"
            required
            :disabled="loading"
          />
        </b-form-group>
        <div class="text-center">
          <b-button type="submit" variant="light">Log In</b-button>
        </div>
        <div class="text-center mt-2">
          <b-link to="/password/reset" class="text-light"
            >Forgot your password</b-link
          >
          |
          <b-link to="/signup" class="text-light">Sign Up</b-link>
        </div>
      </b-form>
    </b-card>
  </div>
</template>

<script>
export default {
  layout: "headless",
  data() {
    return {
      email: "",
      password: "",
      loading: false,
    };
  },
  methods: {
    async login() {
      try {
        this.loading = true;
        await this.$auth.loginWith("local", {
          data: { email: this.email, password: this.password },
        });
      } catch (err) {
        console.log(err.response);
        this.$bvToast.toast(err.response.data.detail, {
          title: "Error while login",
          autoHideDelay: 5000,
          toaster: "b-toaster-top-center",
          variant: "danger",
        });
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
