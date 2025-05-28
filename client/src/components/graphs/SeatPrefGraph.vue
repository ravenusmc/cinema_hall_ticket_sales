<template>
    <div>
        <div ref="seatPrefGraph"></div>
    </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "AgeGraph",
  computed: {
    ...mapGetters("datapage", [
      "seatPreferanceData",
    ]),
  },
  mounted() {
    this.buildSeatPrefGraph();
  },  
  methods: {
  buildSeatPrefGraph() {
    const margin = { top: 50, right: 30, bottom: 50, left: 70 };
    const width = 460 - margin.left - margin.right;
    const height = 400 - margin.top - margin.bottom;

    const svg = d3
      .select(this.$refs.seatPrefGraph)
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    // Extract headers and data
    const headers = this.seatPreferanceData[0].slice(1); // ['Standard', 'VIP', 'Premium']
    const genres = this.seatPreferanceData.slice(1); // rest of the rows

    // Transform to object format for d3.stack
    const data = genres.map((d) => ({
      Genre: d[0],
      Standard: d[1],
      VIP: d[2],
      Premium: d[3],
    }));

    const colors = d3.scaleOrdinal()
      .domain(headers)
      .range(["#1f77b4", "#ff7f0e", "#2ca02c"]);

    const x = d3.scaleBand()
      .domain(data.map(d => d.Genre))
      .range([0, width])
      .padding(0.2);

    svg.append("g")
      .attr("transform", `translate(0,${height})`)
      .call(d3.axisBottom(x));

    const y = d3.scaleLinear()
      .domain([0, d3.max(data, d => d.Standard + d.VIP + d.Premium)])
      .range([height, 0]);

    svg.append("g").call(d3.axisLeft(y));

    // Stack the data
    const stackedData = d3.stack().keys(headers)(data);

    // Tooltip
    const tooltip = d3.select(this.$refs.seatPrefGraph)
      .append("div")
      .style("opacity", 0)
      .attr("class", "tooltip")
      .style("background-color", "white")
      .style("border", "solid 1px gray")
      .style("border-radius", "5px")
      .style("padding", "10px")
      .style("position", "absolute");

    const showTooltip = (event, d, genre, seatType) => {
      tooltip
        .style("opacity", 1)
        .html(`Genre: ${genre}<br>Seat: ${seatType}<br>Count: ${d.data[seatType]}`)
        .style("left", event.pageX + 10 + "px")
        .style("top", event.pageY - 10 + "px");
    };

    const moveTooltip = (event) => {
      tooltip
        .style("left", event.pageX + 10 + "px")
        .style("top", event.pageY - 10 + "px");
    };

    const hideTooltip = () => {
      tooltip.style("opacity", 0);
    };

    svg.selectAll("g.layer")
      .data(stackedData)
      .join("g")
      .attr("fill", d => colors(d.key))
      .selectAll("rect")
      .data(d => d.map(v => ({ ...v, key: d.key })))
      .join("rect")
      .attr("x", d => x(d.data.Genre))
      .attr("y", d => y(d[1]))
      .attr("height", d => y(d[0]) - y(d[1]))
      .attr("width", x.bandwidth())
      .on("mouseover", (event, d) => showTooltip(event, d, d.data.Genre, d.key))
      .on("mousemove", moveTooltip)
      .on("mouseleave", hideTooltip);

    // Legend
    const legend = svg.selectAll(".legend")
      .data(headers)
      .enter()
      .append("g")
      .attr("transform", (d, i) => `translate(0, ${i * 15})`);

    legend.append("rect")
      .attr("x", width - 15)
      .attr("width", 12)
      .attr("height", 12)
      .style("fill", d => colors(d));

    legend.append("text")
      .attr("x", width - 20)
      .attr("y", 6)
      .attr("dy", "0.35em")
      .style("text-anchor", "end")
      .text(d => d);

    // Labels and Title
    svg.append("text")
      .attr("text-anchor", "middle")
      .attr("x", width / 2)
      .attr("y", height + margin.bottom - 10)
      .attr("font-size", "12px")
      .attr("font-weight", "bold")
      .text("Genre");

    svg.append("text")
      .attr("text-anchor", "middle")
      .attr("transform", "rotate(-90)")
      .attr("x", -height / 2)
      .attr("y", -margin.left + 20)
      .attr("font-size", "12px")
      .attr("font-weight", "bold")
      .text("Ticket Sales");

    svg.append("text")
      .attr("text-anchor", "middle")
      .attr("x", width / 2)
      .attr("y", -margin.top / 2 + 10)
      .attr("font-size", "16px")
      .attr("font-weight", "bold")
      .text("Seat Preference by Genre");
  }
}

};

</script>