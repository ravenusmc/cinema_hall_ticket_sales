<template>
  <div>
    <div class="main-background-div">

    </div>
  </div>
</template>

<script>
  export default {
    name: "HomeView",
  }
</script>

<style>
.main-background-div {
  width: 100%;
  height: 100vh; /* Full viewport height */
  background: url("../assets/images/theater_image.jpg") center/cover no-repeat;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -1; /* Keep it behind the content */
  animation: zoomEffect 20s ease-in-out infinite; /* Apply animation */
}

@keyframes zoomEffect {
  0% {
    background-size: 100%; /* Start at normal size */
    background-position: center center; /* Start at the center */
  }
  50% {
    background-size: 120%; /* Zoom in to 120% */
    background-position: center top; /* Move the image upwards */
  }
  100% {
    background-size: 100%; /* Reset to original size */
    background-position: center center; /* Reset to center */
  }
}

</style>