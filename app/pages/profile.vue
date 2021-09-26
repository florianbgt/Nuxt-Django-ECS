<template>
  <div>
    <b-form @submit.prevent="changeEmail">
      <b-form-group id="email" label="Email" label-for="input-email">
        <b-form-input
          v-model="email.value"
          id="input-email"
          type="email"
          placeholder="Enter Email"
          autocomplete="username"
          required
          :disabled="loading || !email.edit"
        />
      </b-form-group>
      <template v-if="email.edit">
        <b-button @click="cancelEmail" variant="danger">Cancel</b-button>
        <b-button type="submit" variant="success">Validate</b-button>
      </template>
    </b-form>
    <template v-if="!email.edit">
      <b-button @click="email.edit = true">Change email</b-button>
      <b-button @click="password.edit = true">Change password</b-button>
    </template>
    <b-modal v-model="password.edit" title="Change password" hide-footer>
      <b-form @submit.prevent="changePassword">
        <b-form-group
          id="oldPassword"
          label="Old password"
          label-for="input-old-password"
        >
          <b-form-input
            v-model="password.old"
            id="input-old-password"
            type="password"
            placeholder="Enter old password"
            autocomplete="current-password"
            required
            :disabled="loading || !password.edit"
          />
        </b-form-group>
        <b-form-group
          id="newPassword"
          label="New password"
          label-for="input-new-password"
        >
          <b-form-input
            v-model="password.new"
            id="input-new-password"
            type="password"
            placeholder="Enter new password"
            autocomplete="new-password"
            required
            :disabled="loading || !password.edit"
          />
        </b-form-group>
        <b-form-group
          id="newPassword2"
          label="New password (again)"
          label-for="input-new-password2"
        >
          <b-form-input
            v-model="password.new2"
            id="input-new-password2"
            type="password"
            placeholder="Enter new password"
            autocomplete="new-password"
            required
            :disabled="loading || !password.edit"
          />
        </b-form-group>
        <b-button @click="cancelPassword" variant="danger">Cancel</b-button>
        <b-button type="submit" variant="success">Validate</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
export default {
  async fetch() {
    this.email.value = this.$auth.user.email;
  },
  data: () => {
    return {
      email: { value: null, edit: false },
      password: { old: null, new: null, new2: null, edit: false },
      loading: false,
    };
  },
  methods: {
    cancelEmail() {
      this.email = { value: this.$auth.user.email, edit: false };
    },
    async changeEmail() {
      try {
        this.loading = true;
        const user = await this.$axios.$put("user/", {
          email: this.email.value,
        });
        await this.$auth.setUser(user);
        this.cancelEmail();
      } catch (err) {
        console.log(err);
        this.$bvToast.toast(err.response.data.email, {
          title: "Error while email change",
          autoHideDelay: 5000,
          toaster: "b-toaster-top-center",
          variant: "danger",
        });
      } finally {
        this.loading = false;
      }
    },
    cancelPassword() {
      this.password = { old: null, new: null, new2: null, edit: false };
    },
    async changePassword() {
      try {
        this.loading = true;
        await this.$axios.$put("password/change/", {
          old_password: this.password.old,
          password: this.password.new,
          password2: this.password.new2,
        });
        this.cancelPassword();
      } catch (err) {
        console.log(err);
        this.$bvToast.toast(
          err.response.data.old_password
            ? err.response.data.old_password.old_password
            : undefined ||
                err.response.data.password ||
                err.response.data.password2,
          {
            title: "Error while password change",
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