const mapURL = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}';
const mapAttribution = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>';
const accessToken = 'pk.eyJ1IjoianN0cm8iLCJhIjoiY2p2OHc5M3I0MDMzYjN5bm1rN2IwY3JqZSJ9.oOQRV6quXqtCiUkk1ldu8g'; 

// Draw map with view set to coordinates (0, 0) and zoomed out all the way
let mymap = L.map('mapid').setView([0, 0], 1);

// Define map layer
function mapLayer(id) {
  return L.tileLayer(mapURL, {
  	attribution: mapAttribution,
  	minZoom: 1,
  	maxZoom: 18,
  	id: id,
  	accessToken: accessToken
 }).addTo(mymap);
}

// Default "streets" view
let currentLayer = mapLayer("mapbox.streets");

// When streets toggle selected, show streets view
document.getElementById("mapbox.streets").addEventListener("click", function(){
  currentLayer.remove();
  currentLayer = mapLayer("mapbox.streets");
}); 

// When satellite toggle selected, show satellite view
document.getElementById("mapbox.satellite").addEventListener("click", function(){
  currentLayer.remove();
  currentLayer = mapLayer("mapbox.satellite");
});