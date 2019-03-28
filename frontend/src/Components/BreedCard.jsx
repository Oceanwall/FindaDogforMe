import React, { Component } from "react";
import Card from "react-bootstrap/Card";
import "../styles/BreedCard.css";
import Container from "react-bootstrap/Container";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import { Link } from 'react-router-dom';
import DefaultImage from "./DefaultImage";

class BreedCard extends Component {
  render() {
    let card_image;
    if (this.props.breed.image_1) {
      card_image = <Card.Img
        variant="top"
        src={this.props.breed.image_1}
        style={{ width: "auto", height: "300px" }}
      />
    }
    else {
      card_image = <DefaultImage
        name={this.props.breed.name}
      />
    }

    return (
      <Card style={{ width: "18rem", height: "40rem" }}  className="mt-4">
        {card_image}
        <Card.Body>
          <Card.Title>{this.props.breed.name}</Card.Title>
          <Card.Text>
            <Container>
              <Row>
                <Col>
                  <p align="left"><b>Group:</b></p>
                </Col>
                <Col xs="auto">
                  <p align="right">{this.props.breed.group}</p>
                </Col>
              </Row>
              <Row>
                <Col>
                  <p align="left"><b>Temperament:</b></p>
                </Col>
                <Col>
                  <p align="right" class="cutoff">{this.props.breed.temperament}</p>
                </Col>
              </Row>
              <Row>
                <Col>
                  <p align="left"><b>Lifespan:</b></p>
                </Col>
                <Col xs="auto">
                  <p align="right">{this.props.breed.min_lifespan} - {this.props.breed.max_lifespan}</p>
                </Col>
              </Row>
              <Row>
                <Col>
                  <p align="left"><b>Height:</b></p>
                </Col>
                <Col xs="auto">
                  <p align="right">{this.props.breed.min_height} - {this.props.breed.max_height}</p>
                </Col>
              </Row>
              <Row>
                <Col>
                  <Link to={`/breeds/${this.props.breed.name}`}>Learn More</Link>
                </Col>
              </Row>
            </Container>
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }
}

export default BreedCard;
