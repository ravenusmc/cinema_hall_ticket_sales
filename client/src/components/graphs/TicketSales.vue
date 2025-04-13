<template>
    <div>
        <h1>Ticket Sales by Movie Genre</h1>
        Bar Chart: Ticket Sales by Movie Genre – Show how many tickets were sold per genre.
        <div ref="TicketSalesByGenre"></div>
    </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "TicketSales",
  computed: {
    ...mapGetters("datapage", [
      "ticketSalesByMovieGenre",
    ]),
  },
  mounted() {
    this.TicketSalesByGenre();
  },  
  methods: {
    TicketSalesByGenre() {
      
      // set the dimensions and margins of the graph
      let margin = { top: 50, right: 30, bottom: 50, left: 70 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the div
      let svg = d3
        .select(this.$refs.TicketSalesByGenre)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
      
      // Add X axis
      let x = d3
        .scaleBand()
        .range([0, width])
        .domain(this.ticketSalesByMovieGenre.map((d) => d[0]))
        .padding(0.2);
      svg
        .append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));
      
      // Add Y axis
      let y = d3
        .scaleLinear()
        .domain([0, d3.max(this.ticketSalesByMovieGenre, (d) => d[1])])
        .range([height, 0]);
      svg.append("g").call(d3.axisLeft(y));

      // Add bars
      let bars = svg
        .selectAll("rect")
        .data(this.ticketSalesByMovieGenre);
      
        // Enter new bars
        bars
          .enter()
          .append("rect")
          .attr("x", (d) => x(d[0]))
          .attr("y", height) // Initial position at the bottom of the chart
          .attr("width", x.bandwidth())
          .attr("height", 0) // Initial height 0 (so it grows with the animation)
          .attr("fill", "#0B90CA")
          // .on("mouseover", showTooltip)
          // .on("mousemove", moveTooltip)
          // .on("mouseleave", hideTooltip)
          .transition() // Apply transition for the animation
          .duration(1500)
          .attr("y", (d) => y(d[1])) // Final Y position
          .attr("height", (d) => height - y(d[1])); // Final height after transition


    }
  }
};
</script>

<style scoped>
</style>