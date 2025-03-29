<template>
  <div>
    <div class="main-background-div">
      <div class="inner-div">
        <h1 class="title">Welcome</h1>
        <hr>
        <h3 class="sub-title">Examine The Data</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style scoped>

.main-background-div {
  width: 100%;
  height: 100vh; /* Full viewport height */
  background: url("../assets/images/theater_image.jpg") center/cover no-repeat;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -1; /* Keep it behind the content */
  animation: zoomEffect 5s ease-in forwards; /* Apply animation and keep final state */
}

@keyframes zoomEffect {
  0% {
    background-size: 100%; /* Start at normal size */
    background-position: center center; /* Start at the center */
  }
  100% {
    background-size: 120%; /* Zoom in to 120% and stay */
    background-position: center top; /* Move the image upwards */
  }
}

.inner-div {
  width: 45%;
  position: absolute;
  top: 55%;
  left: 48%;
  transform: translate(-50%, -50%);
  border: 2px solid black;
  padding: 20px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 15px;
  text-align: center;
  opacity: 0; 
  animation: fadeIn 1s ease-in forwards;
  animation-delay: 5s; 
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
    top: 45%; /* Ensure it remains centered */
  }
}

.title {
  text-transform: uppercase;
  font-size: 5rem;
}

.sub-title {
  text-transform: uppercase;
  font-size: 3rem;
}

</style>