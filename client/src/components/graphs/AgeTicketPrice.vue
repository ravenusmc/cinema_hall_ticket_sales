<template>
    <div>
      <div ref="AgeTicketPriceGraph"></div>
    </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "AgeGraph",
  computed: {
    ...mapGetters("datapage", [
      "ageTicketPriceData",
    ]),
  },
  mounted() {
    this.buildAgeTicketPriceDataGraph();
  },  
  methods: {
    buildAgeTicketPriceDataGraph() {
      const margin = { top: 20, right: 30, bottom: 40, left: 50 };
      const width = 800 - margin.left - margin.right;
      const height = 400 - margin.top - margin.bottom;

      const svg = d3
        .select(this.$refs.AgeTicketPriceGraph)
        .append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      // Scales
      const x = d3
        .scaleLinear()
        .domain(d3.extent(this.ageTicketPriceData, d => d.Age))
        .range([0, width]);

      const y = d3
        .scaleLinear()
        .domain(d3.extent(this.ageTicketPriceData, d => d.Predicted_Ticket_Price))
        .range([height, 0]);

      // Axes
      svg.append('g')
        .attr('transform', `translate(0,${height})`)
        .call(d3.axisBottom(x));

      svg.append('g')
        .call(d3.axisLeft(y));

      // Line generator
      const line = d3.line()
        .x(d => x(d.Age))
        .y(d => y(d.Predicted_Ticket_Price));

      // Line path
      svg.append('path')
        .datum(this.ageTicketPriceData)
        .attr('fill', 'none')
        .attr('stroke', 'steelblue')
        .attr('stroke-width', 2)
        .attr('d', line);

      // Optional: Add dots
      svg.selectAll('circle')
        .data(this.ageTicketPriceData)
        .enter()
        .append('circle')
        .attr('cx', d => x(d.Age))
        .attr('cy', d => y(d.Predicted_Ticket_Price))
        .attr('r', 3)
        .attr('fill', 'orange');
    }
  }

};

</script>