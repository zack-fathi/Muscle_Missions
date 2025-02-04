import React from "react";
import { Form, Button, Card } from "react-bootstrap";

function WorkoutForm({ title, fields, onChange, onSubmit, isSubmitting }) {
  return (
    <Card>
      <Card.Body>
        <h2 className="text-center mb-4">{title}</h2>
        <Form onSubmit={onSubmit}>
          {fields.map((field, index) => {
            if (field.type === "select") {
              return (
                <Form.Group className="mb-3" key={index}>
                  <Form.Label>{field.label}</Form.Label>
                  <Form.Select
                    name={field.name}
                    value={field.value}
                    onChange={onChange}
                    required={field.required}
                  >
                    <option value="">{field.placeholder}</option>
                    {field.options.map((option, idx) => (
                      <option key={idx} value={option.value}>
                        {option.label}
                      </option>
                    ))}
                  </Form.Select>
                </Form.Group>
              );
            } else if (field.type === "checkbox") {
              return (
                <Form.Group className="mb-3" key={index}>
                  <Form.Label>{field.label}</Form.Label>
                  {field.options.map((option, idx) => (
                    <Form.Check
                      key={idx}
                      type="checkbox"
                      id={option.value}
                      name={field.name}
                      value={option.value}
                      label={option.label}
                      onChange={onChange}
                    />
                  ))}
                </Form.Group>
              );
            } else {
              return (
                <Form.Group className="mb-3" key={index}>
                  <Form.Label>{field.label}</Form.Label>
                  <Form.Control
                    type={field.type}
                    name={field.name}
                    placeholder={field.placeholder}
                    value={field.value}
                    onChange={onChange}
                    required={field.required}
                  />
                </Form.Group>
              );
            }
          })}
          <Button
            type="submit"
            variant="primary"
            className="w-100"
            disabled={isSubmitting}
          >
            {isSubmitting ? "Submitting..." : "Submit"}
          </Button>
        </Form>
      </Card.Body>
    </Card>
  );
}

export default WorkoutForm;
