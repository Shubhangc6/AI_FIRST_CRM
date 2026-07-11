import { useState } from "react";
import api from "../services/api";

function InteractionForm() {
  const [form, setForm] = useState({
    doctor_name: "",
    hospital: "",
    product: "",
    meeting_date: "",
    summary: "",
    follow_up: "",
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await api.post("/interactions", form);
      alert("Interaction Saved Successfully!");
      console.log(res.data);

      setForm({
        doctor_name: "",
        hospital: "",
        product: "",
        meeting_date: "",
        summary: "",
        follow_up: "",
      });
    } catch (err) {
      console.error(err);
      alert("Error saving interaction");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Interaction</h2>

      <input
        type="text"
        name="doctor_name"
        placeholder="Doctor Name"
        value={form.doctor_name}
        onChange={handleChange}
      />

      <br /><br />

      <input
        type="text"
        name="hospital"
        placeholder="Hospital"
        value={form.hospital}
        onChange={handleChange}
      />

      <br /><br />

      <input
        type="text"
        name="product"
        placeholder="Product"
        value={form.product}
        onChange={handleChange}
      />

      <br /><br />

      <label>Meeting Date</label><br />
      <input
        type="date"
        name="meeting_date"
        value={form.meeting_date}
        onChange={handleChange}
      />

      <br /><br />

      <textarea
        name="summary"
        placeholder="Summary"
        rows="4"
        cols="40"
        value={form.summary}
        onChange={handleChange}
      />

      <br /><br />

      <label>Follow-up Date</label><br />
      <input
        type="date"
        name="follow_up"
        value={form.follow_up}
        onChange={handleChange}
      />

      <br /><br />

      <button type="submit">Save Interaction</button>
    </form>
  );
}

export default InteractionForm;