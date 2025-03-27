<template>
  <div>
    <div class="main-background-div">
      <div class="inner-div">
        <h1>Welcome</h1>
        <p>Examine The Data</p>
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
  animation: zoomEffect 15s ease-in forwards; /* Apply animation and keep final state */
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
  position: absolute;
  top: 60%;
  left: 50%;
  transform: translate(-50%, -50%);
  border: 2px solid black;
  padding: 20px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 15px;
  text-align: center;
  opacity: 0; /* Initially hidden */
  animation: fadeIn 1s ease-in forwards;
  animation-delay: 15s; /* Delays appearance until zoom is complete */
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
    top: 50%; /* Ensure it remains centered */
  }
}

</style>