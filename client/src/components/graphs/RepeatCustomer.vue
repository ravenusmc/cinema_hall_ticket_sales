<template>
    <div>
      <div ref="repeatCustomerGraph"></div>
    </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "AgeGraph",
  computed: {
    ...mapGetters("datapage", [
      "repeatCustomersData",
    ]),
  },
  mounted() {
    this.buildRepeatCustomerGraph();
  },  
  methods: {
  buildRepeatCustomerGraph() {
    
    // set the dimensions and margins of the graph
    let margin = { top: 50, right: 30, bottom: 50, left: 70 };
    let width = 460 - margin.left - margin.right;
    let height = 400 - margin.top - margin.bottom;
    let radius = Math.min(width, height) / 2; // <-- [CHANGED] Define radius for pie chart

    // append the svg object to the div
    let svg = d3
      .select(this.$refs.repeatCustomerGraph)
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr(
        "transform",
        "translate(" + (width / 2 + margin.left) + "," + (height / 2 + margin.top) + ")"
      ); // <-- [CHANGED] Move g to center for pie chart

    // Create a tooltip div
    let tooltip = d3
      .select(this.$refs.repeatCustomerGraph)
      .append("div")
      .style("opacity", 0)
      .attr("class", "tooltip")
      .style("background-color", "white")
      .style("border", "solid")
      .style("border-width", "1px")
      .style("border-radius", "5px")
      .style("padding", "10px")
      .style("position", "absolute");

    // Tooltip functions
    let showTooltip = function (event, d) {
      tooltip
        .style("opacity", 1)
        .html("Age Group: " + d.data[0] + "<br>Count: " + d.data[1]) // <-- [CHANGED] Access data differently for pie
        .style("left", event.pageX + 10 + "px")
        .style("top", event.pageY - 10 + "px");
    };

    let moveTooltip = function (event) {
      tooltip
        .style("left", event.pageX + 10 + "px")
        .style("top", event.pageY - 10 + "px");
    };

    let hideTooltip = function () {
      tooltip.style("opacity", 0);
    };

    // Generate the pie
    let pie = d3.pie()
      .value(function(d) { return d[1]; }); // <-- [CHANGED] Pie values based on counts

    let data_ready = pie(this.repeatCustomersData); // <-- [CHANGED] Prepare the pie chart data

    // Shape generator
    let arc = d3.arc()
      .innerRadius(0) // <-- [CHANGED] Set to 0 for regular pie (not donut)
      .outerRadius(radius);

    // Color scale
    let color = d3.scaleOrdinal()
      .domain(this.repeatCustomersData.map(d => d[0]))
      .range(d3.schemeCategory10); // <-- [NEW] Color for each slice

    // Build the pie chart
    svg
      .selectAll('slices')
      .data(data_ready)
      .enter()
      .append('path')
      .attr('d', arc)
      .attr('fill', d => color(d.data[0]))
      .attr("stroke", "white")
      .style("stroke-width", "2px")
      .on("mouseover", showTooltip)
      .on("mousemove", moveTooltip)
      .on("mouseleave", hideTooltip);

    // Add labels inside the slices
    svg
      .selectAll('labels')
      .data(data_ready)
      .enter()
      .append('text')
      .text(d => d.data[0])
      .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
      .style("text-anchor", "middle")
      .style("font-size", "12px");

    // Add title
    svg
      .append("text")
      .attr("text-anchor", "middle")
      .attr("y", -height / 2 - margin.top / 2 + 20) // <-- [CHANGED] Adjust title position for pie
      .attr("x", 0)
      .attr("font-size", "16px")
      .attr("font-weight", "bold")
      .text("Repeat Customers");
    }
  }
}

</script>