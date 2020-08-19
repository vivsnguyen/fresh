import React, { Component } from 'react';
import { Map, GoogleApiWrapper } from 'google-maps-react';
import { config } from '../config'

const mapStyles = {
  width: '100%',
  height: '70%'
};

export class MapContainer extends Component {
  render() {
    return (
      <Map
        google={this.props.google}
        zoom={13}
        style={mapStyles}
        initialCenter={{
         lat: 37.8044,
         lng: -122.2712
        }}
      />
    );
  }
}

export default GoogleApiWrapper({
  apiKey: config.GOOGLE_API_KEY
})(MapContainer);