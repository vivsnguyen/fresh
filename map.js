"use strict";

const api=config.GOOGLE_API_KEY;
var urlRoot="https://maps.googleapis.com/maps/api/js?key=";
var urlEnd="&callback=initMap&libraries=&v=weekly";
document.getElementById('googleMaps').src = urlRoot+api+urlEnd;

function initMap() {
    let place = {lat: 37.8044, lng: -122.2712};
    let map = new google.maps.Map(document.getElementById("map"), {
      center: place,
      zoom: 10
    });
    let marker = new google.maps.Marker({position: place, map: map});
  }
