var w = 300;
var h = 100;
TransferRate = [
    {"min":5, "NumPackets":15},
    {"min":10, "NumPackets":18},
    {"min":15, "NumPackets":4},
    {"min":20, "NumPackets":32},
    {"min":25, "NumPackets":45},
    {"min":30, "NumPackets":30},
    {"min":35, "NumPackets":6},
    {"min":40, "NumPackets":90},
    {"min":45, "NumPackets":100},
    {"min":50, "NumPackets":36},
    {"min":55, "NumPackets":45}


];

var lineFun = d3.svg.line()
.x(function(d) { return d.min*2;})
.y(function(d) {return d.NumPackets; })
.interpolate("linear");

var svg =
    d3.select("body").append("svg").attr({
        width:w, height:h
    });
var viz = svg.append("path")
    .attr({
    d: lineFun(TransferRate),
        "stroke": "purple",
    "stroke-width": 2,
    "fill": "none"
        });
