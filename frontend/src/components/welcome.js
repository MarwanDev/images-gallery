import React from 'react';
import { Jumbotron, Button } from 'react-bootstrap';
const Welcome = () => (
  <Jumbotron>
    <h1>Images Gallery</h1>
    <p>
      This is a simple application for displaying images from unsplash. All you
      need to do is search for any topic to reach relevant pictures.
    </p>
    <p>
      <Button variant="primary" href="https://unsplash.com" target="_blank">
        Learn more
      </Button>
    </p>
  </Jumbotron>
);

export default Welcome;
