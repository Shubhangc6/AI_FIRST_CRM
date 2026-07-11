import { useEffect, useState } from "react";
import api from "../services/api";

function InteractionList() {
  const [interactions, setInteractions] = useState([]);

  const fetchData = async () => {
    try {
      const res = await api.get("/interactions");
      setInteractions(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <>
      <h2>Interactions</h2>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Doctor</th>
            <th>Hospital</th>
            <th>Product</th>
            <th>Summary</th>
          </tr>
        </thead>

        <tbody>
          {interactions.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.doctor_name}</td>
              <td>{item.hospital}</td>
              <td>{item.product}</td>
              <td>{item.summary}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
}

export default InteractionList;