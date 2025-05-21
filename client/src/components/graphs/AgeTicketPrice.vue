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

  // Your data: array of [Age, Ticket_Price]
  const data = this.ageTicketPriceData; 

  // Separate X and y for regression calculation
  const X = data.map(d => d[0]);
  const y = data.map(d => d[1]);

  // Calculate linear regression parameters (slope and intercept)
  const n = data.length;
  const sumX = d3.sum(X);
  const sumY = d3.sum(y);
  const sumXY = d3.sum(data, d => d[0] * d[1]);
  const sumX2 = d3.sum(X, d => d * d);

  const slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
  const intercept = (sumY - slope * sumX) / n;

  // Scales
  const x = d3
    .scaleLinear()
    .domain(d3.extent(X))
    .range([0, width]);

  const yScale = d3
    .scaleLinear()
    .domain(d3.extent(y))
    .range([height, 0]);

    // Axes
    svg.append('g')
      .attr('transform', `translate(0,${height})`)
      .call(d3.axisBottom(x));

    svg.append('g')
      .call(d3.axisLeft(yScale));

    // Plot data points
    svg.selectAll('circle')
      .data(data)
      .enter()
      .append('circle')
      .attr('cx', d => x(d[0]))
      .attr('cy', d => yScale(d[1]))
      .attr('r', 3)
      .attr('fill', 'orange');

    // Regression line points
    const xVals = d3.extent(X);
    const linePoints = xVals.map(xVal => {
      return { x: xVal, y: slope * xVal + intercept };
    });

    // Line generator for regression line
    const line = d3.line()
      .x(d => x(d.x))
      .y(d => yScale(d.y));

    // Draw regression line
    svg.append('path')
      .datum(linePoints)
      .attr('fill', 'none')
      .attr('stroke', 'steelblue')
      .attr('stroke-width', 2)
      .attr('d', line);
    }
  }

};

</script>