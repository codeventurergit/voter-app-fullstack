import React, { useState, useEffect } from 'react';
import axios from 'axios';

// API Gateway URL
const API_BASE = "https://u1mfkd0gxl.execute-api.us-east-1.amazonaws.com/Prod/voters/"; 

function App() {
  const [voters, setVoters] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedVoter, setSelectedVoter] = useState(null);
  const [aiStrategy, setAiStrategy] = useState("");

  // 1. Fetch Voters on Load
  useEffect(() => {
    const fetchVoters = async () => {
      try {
        const res = await axios.get(`${API_BASE}/voters`);
        setVoters(res.data);
      } catch (err) {
        console.error("Error fetching voters:", err);
      }
    };
    fetchVoters();
  }, []);

  // 2. Trigger AI Insight
  const getAIInsight = async (voter) => {
    setLoading(true);
    setAiStrategy("");
    setSelectedVoter(voter);
    
    try {
      const res = await axios.post(`${API_BASE}/voters/${voter.id}/ai-strategy`);
      setAiStrategy(res.data.strategy);
    } catch (err) {
      setAiStrategy("Error: Could not connect to AI service. Ensure Ollama is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <h1>Voter Insights & AI Strategy</h1>
        <p>Full-Stack Python + React + Ollama Demo</p>
      </header>

      <main style={styles.main}>
        <section style={styles.listSection}>
          <h2>Voter Records</h2>
          <div style={styles.cardGrid}>
            {voters.map(voter => (
              <div key={voter.id} style={styles.card}>
                <h3>{voter.name || `Voter ${voter.id}`}</h3>
                <p><strong>Demographics:</strong> {voter.demographics}</p>
                <button 
                  onClick={() => getAIInsight(voter)}
                  style={styles.button}
                >
                  Generate AI Strategy
                </button>
              </div>
            ))}
          </div>
        </section>

        <section style={styles.aiSection}>
          <h2>AI Strategy Output</h2>
          {selectedVoter && (
            <div style={styles.insightBox}>
              <h3>Targeting: {selectedVoter.name}</h3>
              {loading ? (
                <p style={styles.pulse}>AI is analyzing voter behavior...</p>
              ) : (
                <p style={styles.resultText}>{aiStrategy || "Select a voter to generate a strategy."}</p>
              )}
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

// Simple Inline Styles for a Professional Look
const styles = {
  container: { padding: '2rem', fontFamily: 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif', backgroundColor: '#f4f7f6', minHeight: '100vh' },
  header: { borderBottom: '2px solid #333', marginBottom: '2rem', paddingBottom: '1rem' },
  main: { display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' },
  card: { backgroundColor: '#fff', padding: '1.5rem', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)', marginBottom: '1rem' },
  button: { backgroundColor: '#007bff', color: '#fff', border: 'none', padding: '0.5rem 1rem', borderRadius: '4px', cursor: 'pointer', marginTop: '10px' },
  insightBox: { backgroundColor: '#e9ecef', padding: '2rem', borderRadius: '12px', borderLeft: '5px solid #28a745' },
  pulse: { fontStyle: 'italic', color: '#666' },
  resultText: { lineHeight: '1.6', fontSize: '1.1rem', color: '#333' }
};

export default App;