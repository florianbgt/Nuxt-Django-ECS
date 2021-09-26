<template>
  <div>
    <div style="height: 65px" />
    <b-navbar toggleable="md" fixed="top" type="dark" variant="dark">
      <b-container>
        <b-navbar-brand to="/">
          <img
            src="/icon.png"
            height="40px"
            width="50px"
            alt="logo"
            class="d-inline-block bg-light p-1 rounded"
          />
          <span class="ml-2"> Awesome Recipes! </span>
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item to="/"> Home </b-nav-item>
            <b-nav-item to="/recipes"> Recipes </b-nav-item>
            <b-nav-item to="/profile"> Profile </b-nav-item>
            <b-nav-item @click="logout"> Logout </b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
  </div>
</template>

<script>
export default {
  methods: {
    async logout() {
      try {
        this.$auth.logout();
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>
