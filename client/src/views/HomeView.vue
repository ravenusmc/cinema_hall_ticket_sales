<template>
  <div>
    <div class="main-background-div">
      <div class="inner-graph">
        <h1>Welcome</h1>
        <p>See The Data</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
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
  animation: zoomEffect 20s ease-in; /* Apply animation */
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

.inner-graph {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border: 2px solid red;
  padding: 20px;
  background: rgba(255, 255, 255, 0.8);
  text-align: center;
  opacity: 0; /* Initially invisible */
  animation: fadeIn 1s ease-in forwards;
  animation-delay: 7s; /* Delays appearance */
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
</style>