<template>
    <div>
        <div ref="seatTicketPriceGraph"></div>
    </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "AgeGraph",
  computed: {
    ...mapGetters("datapage", [
      "ticketPriceSeatPrice",
    ]),
  },
  mounted() {
    this.buildSeatTicketPriceGraph();
  },  
  methods: {
    buildSeatTicketPriceGraph() {
      const data = this.ticketPriceSeatPrice;

      let margin = { top: 50, right: 30, bottom: 50, left: 70 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      let svg = d3
        .select(this.$refs.seatTicketPriceGraph)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

      let x = d3
        .scaleBand()
        .range([0, width])
        .domain(data.map((d) => d.seat_type))
        .padding(0.4);
      svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

      let y = d3
        .scaleLinear()
        .domain([0, d3.max(data, (d) => d.max)])
        .range([height, 0]);
      svg.append("g").call(d3.axisLeft(y));

      // Tooltip
      let tooltip = d3
        .select(this.$refs.seatTicketPriceGraph)
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("background-color", "white")
        .style("border", "solid 1px black")
        .style("border-radius", "5px")
        .style("padding", "10px")
        .style("position", "absolute");

      const showTooltip = (event, d) => {
        tooltip
          .style("opacity", 1)
          .html(
            `<strong>${d.seat_type}</strong><br>
            Min: ${d.min}<br>
            Q1: ${d.q1}<br>
            Median: ${d.median}<br>
            Q3: ${d.q3}<br>
            Max: ${d.max}`
          )
          .style("left", event.pageX + 10 + "px")
          .style("top", event.pageY - 28 + "px");
      };

      const moveTooltip = (event) => {
        tooltip.style("left", event.pageX + 10 + "px").style("top", event.pageY - 28 + "px");
      };

      const hideTooltip = () => tooltip.style("opacity", 0);

      // Draw boxplot elements for each seat type
      data.forEach((d) => {
        let center = x(d.seat_type) + x.bandwidth() / 2;
        let boxWidth = 40;

      // Vertical line (min to max)
      svg.append("line")
        .attr("x1", center)
        .attr("x2", center)
        .attr("y1", y(d.min))
        .attr("y2", y(d.max))
        .attr("stroke", "black");

      // Rect for IQR (q1 to q3)
      svg.append("rect")
        .attr("x", center - boxWidth / 2)
        .attr("y", y(d.q3))
        .attr("height", y(d.q1) - y(d.q3))
        .attr("width", boxWidth)
        .attr("stroke", "black")
        .attr("fill", "#0B90CA")
        .on("mouseover", (event) => showTooltip(event, d))
        .on("mousemove", moveTooltip)
        .on("mouseleave", hideTooltip);

      // Median line
      svg.append("line")
        .attr("x1", center - boxWidth / 2)
        .attr("x2", center + boxWidth / 2)
        .attr("y1", y(d.median))
        .attr("y2", y(d.median))
        .attr("stroke", "black");
    });

  // Add labels and title
  svg.append("text")
    .attr("text-anchor", "middle")
    .attr("x", width / 2)
    .attr("y", height + margin.bottom - 10)
    .attr("font-size", "12px")
    .attr("font-weight", "bold")
    .text("Seat Type");

  svg.append("text")
    .attr("text-anchor", "middle")
    .attr("transform", "rotate(-90)")
    .attr("x", -height / 2)
    .attr("y", -margin.left + 20)
    .attr("font-size", "12px")
    .attr("font-weight", "bold")
    .text("Ticket Price");

  svg.append("text")
    .attr("text-anchor", "middle")
    .attr("x", width / 2)
    .attr("y", -margin.top / 2 + 10)
    .attr("font-size", "16px")
    .attr("font-weight", "bold")
    .text("Ticket Price by Seat Type");
    }
  
  }

};

</script>