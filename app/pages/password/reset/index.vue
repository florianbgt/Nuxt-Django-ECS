<template>
  <div class="w-100" style="max-width: 500px">
    <b-card title="Password reset" class="bg-secondary text-light">
      <b-form v-if="!sent" @submit.prevent="resetPassword">
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
        <div class="text-center">
          <b-button to="/login" variant="light">Back to Login</b-button>
          <b-button type="submit" variant="success">Send reset link</b-button>
        </div>
      </b-form>
      <template v-else>
        <p>An Password reset link have been sent to <strong>{{ email }}</strong></p>
        <p>
          Did not receive the link?
          <b-button @click="sent = false" size="sm" variant="light"
            >Send a new one</b-button
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
  data() {
    return {
      email: "",
      sent: false,
      loading: false,
    };
  },
  methods: {
    async resetPassword() {
      try {
        this.loading = true;
        await this.$axios.$post("password/reset/", { email: this.email });
        this.sent = true;
      } catch (err) {
        console.log(err.response);
        this.$bvToast.toast(err.response.data.email, {
          title: "Error while requesting password reset",
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