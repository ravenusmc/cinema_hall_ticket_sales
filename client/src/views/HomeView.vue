<template>
  <div class="main-container">
    <div class="content">
      <h1 class="title">Welcome</h1>
      <hr />
      <h3 class="sub-title">Examine The Data</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style scoped>
/* Full-page container */
.main-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
  background: url("../assets/images/theater_image.jpg") center/cover no-repeat;
  animation: zoomEffect 5s ease-in forwards;
  position: relative;
}

/* Zoom effect */
@keyframes zoomEffect {
  0% {
    background-size: 100%;
  }
  100% {
    background-size: 120%;
  }
}

/* Centered content */
.content {
  display: grid;
  place-items: center;
  width: min(80%, 600px); /* Adaptive width */
  background: rgba(255, 255, 255, 0.85);
  padding: 2rem;
  border-radius: 15px;
  text-align: center;
  border: 2px solid black;
  opacity: 0;
  animation: fadeIn 1s ease-in forwards;
  animation-delay: 4s; /* Delayed appearance */
}

/* Fade-in animation */
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: scale(0.8);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

/* Responsive Typography */
.title {
  text-transform: uppercase;
  font-size: clamp(2rem, 5vw, 4rem);
  line-height: 1.2;
}

.sub-title {
  text-transform: uppercase;
  font-size: clamp(1.5rem, 3vw, 3rem);
  line-height: 1.2;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .content {
    width: 90%;
    padding: 1.5rem;
  }
}

@media (max-width: 480px) {
  .content {
    width: 95%;
    padding: 1rem;
  }
}
</style>


