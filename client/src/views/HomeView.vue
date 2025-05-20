<template>
  <div class="main-container">
    <div class="content">
      <h1 class="title">Welcome</h1>
      <hr />
      <h3 class="sub-title"><router-link class="link-style" to="/data">Examine The Data</router-link></h3>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "HomeView",
  mounted() {
    this.setUpDataForGraphs();
  },  
  methods: {
    ...mapActions("datapage", ["getDataForGraphs"]),
    setUpDataForGraphs() {
      this.getDataForGraphs();
    }
  }
};
</script>

<style scoped>
/* Full-page container with overlay */
.main-container {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
  background: url("../assets/images/theater_image.jpg") center/cover no-repeat;
  overflow: hidden;
  animation: zoomEffect 6s ease-in-out forwards;
}

/* Soft dark overlay */
.main-container::before {
  content: "";
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.6); /* dark overlay */
  backdrop-filter: blur(4px);
  z-index: 1;
}

/* Zoom animation */
@keyframes zoomEffect {
  0% {
    background-size: 100%;
  }
  100% {
    background-size: 115%;
  }
}

/* Centered content */
.content {
  position: relative;
  z-index: 2;
  display: grid;
  place-items: center;
  width: min(85%, 650px);
  background: rgba(255, 255, 255, 0.1);
  padding: 2.5rem;
  border-radius: 20px;
  text-align: center;
  border: 1.5px solid rgba(255, 255, 255, 0.4);
  backdrop-filter: blur(10px);
  box-shadow: 0 0 25px rgba(255, 255, 255, 0.15);
  animation: fadeIn 1.5s ease-out forwards;
  animation-delay: 3s;
  opacity: 0;
}

/* Fade-in with scale */
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: scale(0.85);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

/* Title styling */
.title {
  text-transform: uppercase;
  font-size: clamp(2.5rem, 6vw, 4rem);
  line-height: 1.2;
  color: #ffffff;
  text-shadow: 0 0 10px rgba(255,255,255,0.5);
  margin-bottom: 1rem;
}

/* Subtitle link */
.sub-title {
  text-transform: uppercase;
  font-size: clamp(1.4rem, 4vw, 2.5rem);
  line-height: 1.3;
  margin-top: 0.5rem;
}

.link-style {
  color: #ffeaa7;
  text-decoration: none;
  font-weight: bold;
  transition: color 0.3s ease, text-shadow 0.3s ease;
}

.link-style:hover {
  color: #fab1a0;
  text-shadow: 0 0 8px rgba(255,255,255,0.6);
}

/* Horizontal rule styling */
hr {
  width: 60%;
  border: 0;
  height: 1px;
  background: linear-gradient(to right, #ffffff33, #ffffffaa, #ffffff33);
  margin: 1.2rem 0;
}

/* Responsive tweaks */
@media (max-width: 768px) {
  .content {
    width: 90%;
    padding: 2rem;
  }
}

@media (max-width: 480px) {
  .content {
    width: 95%;
    padding: 1.5rem;
  }
}

</style>


