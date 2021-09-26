<template>
  <div class="w-100" style="max-width: 500px">
    <b-card title="Password reset" class="bg-secondary text-light">
      <b-form v-if="tokenIsValid" @submit.prevent="resetPassword">
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
          label-for="input-password2"
        >
          <b-form-input
            v-model="password2"
            id="input-password2"
            type="password"
            placeholder="Enter Password"
            autocomplete="new-password"
            required
            :disabled="loading"
          />
        </b-form-group>
        <div class="text-center">
          <b-button type="submit" variant="success">Reset password</b-button>
        </div>
      </b-form>
      <template v-else>
        <p>
          You need a valid link to reset your password
          <b-button to="/password/reset" size="sm" variant="light"
            >Request one</b-button
          >
        </p>
      </template>
    </b-card>
  </div>
</template>

<script>
export default {
  auth: "guest",
  layout: "headless",
  async fetch() {
    await this.validateToken();
  },
  data() {
    return {
      password: null,
      password2: null,
      tokenIsValid: null,
      loading: false,
    };
  },
  computed: {
    token() {
      return this.$route.query.token;
    },
  },
  methods: {
    async validateToken() {
      try {
        await this.$axios.$post("password/reset/validate_token/", {
          token: this.token,
        });
        this.tokenIsValid = true;
      } catch (err) {
        console.log(err.response.data);
      }
    },
    async resetPassword() {
      try {
        this.loading = true;
        if (this.password == this.password2) {
          await this.$axios.$post("password/reset/confirm/", {
            password: this.password,
            token: this.token,
          });
          this.$router.push("/login");
        } else {
          this.$bvToast.toast("Password fields did not match", {
            title: "Error while reseting password",
            autoHideDelay: 5000,
            toaster: "b-toaster-top-center",
            variant: "danger",
          });
        }
      } catch (err) {
        console.log(err.response.status);
        this.$bvToast.toast(
          err.response.data.password || "An error occured",
          {
            title: "Error while reseting password",
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