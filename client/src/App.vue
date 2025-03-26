<template>
  <div id="app" class="layout">
    <!-- <NavBar /> -->
    <NavBar v-if="$route.name !== 'home'" />
    <router-view></router-view>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
import NavBar from "./components/common/NavBar.vue";

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>

<style>
/* Ensure no margin or padding disturbs the layout */
body, html {
  margin: 0;
  padding: 0;
  height: 100%; /* Ensure the height covers the full viewport */
}

.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Full viewport height */
}


</style>
