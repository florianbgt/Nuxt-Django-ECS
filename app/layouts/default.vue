<template>
  <div class="d-flex flex-column text-dark" style="min-height: 100vh">
    <Header />
    <b-container fluid class="bg-light py-4" style="flex: 1">
      <b-container class="px-0">
        <Nuxt />
      </b-container>
    </b-container>
    <Footer />
  </div>
</template>