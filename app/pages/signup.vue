<template>
  <div class="w-100" style="max-width: 500px">
    <b-card title="Sign Up" class="bg-secondary text-light">
      <b-form @submit.prevent="signup">
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
        <b-form-group
          id="password"
          label="Password"
          label-for="input-password"
        >
          <b-form-input
            v-model="password"
            id="input-password"
            type="password"
            placeholder="Enter Password"
            autocomplete="new-password"
            required
            :disabled="loading"
          />
        </b-form-group>
        <b-form-group
          id="password2"
          label="Password"
          label-for="input-password"
        >
          <b-form-input
            v-model="password2"
            id="input-password2"
            type="password"
            placeholder="Repeat Password"
            autocomplete="new-password"
            required
            :disabled="loading"
          />
        </b-form-group>
        <div class="text-center">
          <b-button type="submit" variant="light">Sign Up</b-button>
        </div>
        <div class="text-center mt-2">
          <b-link to="/login" class="text-light">Already have an account? Log In instead</b-link>
        </div>
      </b-form>
    </b-card>
  </div>
</template>

<script>
export default {
  auth: "guest",
  layout: "headless",
  data() {
    return {
      email: "",
      password: "",
      password2: "",
      loading: false,
    };
  },
  methods: {
    async signup() {
      try {
        this.loading = true;
        this.$axios.setHeader("Authorization", null);
        await this.$axios.$post("signup/", {
          email: this.email,
          password: this.password,
          password2: this.password2,
        });
        await this.$auth.loginWith("local", {
          data: { email: this.email, password: this.password },
        });
      } catch (err) {
        console.log(err.response);
        this.$bvToast.toast(
          err.response.data.email ||
            err.response.data.password ||
            err.response.data.password2,
          {
            title: "Error while signup",
            autoHideDelay: 5000,
            toaster: "b-toaster-top-center",
            variant: "danger",
          }
        );
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>