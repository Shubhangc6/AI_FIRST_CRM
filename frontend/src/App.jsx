import InteractionForm from "./components/InteractionForm";
import InteractionList from "./components/InteractionList";

function App() {
  return (
    <div style={{ width: "80%", margin: "30px auto" }}>
      <h1>AI First CRM</h1>

      <InteractionForm />

      <hr />

      <InteractionList />
    </div>
  );
}

export default App;