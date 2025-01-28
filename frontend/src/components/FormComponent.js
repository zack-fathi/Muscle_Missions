import React from "react";
import { Form, Button } from "react-bootstrap";

function FormComponent({ title, fields, onSubmit, submitButtonText }) {
  return (
    <div>
      <h4 className="card-title mb-4 mt-1 text-center">{title}</h4>
      <Form onSubmit={onSubmit}>
        {fields.map((field, index) => {
          if (field.type === "select") {
            return (
              <Form.Group className="mb-3" controlId={field.id} key={index}>
                <Form.Label>{field.label}</Form.Label>
                <Form.Select name={field.name} required={field.required}>
                  {field.options.map((option, idx) => (
                    <option key={idx} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </Form.Select>
              </Form.Group>
            );
          } else if (field.type === "radio") {
            return (
              <Form.Group className="mb-3" key={index}>
                <Form.Label>{field.label}</Form.Label>
                {field.options.map((option, idx) => (
                  <Form.Check
                    key={idx}
                    type="radio"
                    id={`${field.id}-${idx}`}
                    label={option.label}
                    name={field.name}
                    value={option.value}
                    required={field.required}
                  />
                ))}
              </Form.Group>
            );
          } else {
            return (
              <Form.Group className="mb-3" controlId={field.id} key={index}>
                <Form.Label>{field.label}</Form.Label>
                <Form.Control
                  type={field.type}
                  placeholder={field.placeholder}
                  name={field.name}
                  required={field.required}
                />
              </Form.Group>
            );
          }
        })}
        <Button type="submit" className="btn btn-primary btn-block w-100">
          {submitButtonText}
        </Button>
      </Form>
    </div>
  );
}

export default FormComponent;
