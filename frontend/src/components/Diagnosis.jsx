import { useState } from 'react';
import { Box, Textarea, Button, Heading } from '@chakra-ui/react';
import axios from 'axios';

export default function Diagnosis() {
  const [input, setInput] = useState('');
  const [result, setResult] = useState(null);

  const analyzeSymptoms = async () => {
    try {
      const response = await axios.post('/api/analyze', { symptoms: input });
      setResult(response.data);
    } catch (error) {
      console.error("Analysis failed:", error);
    }
  };

  return (
    <Box p={8}>
      <Heading mb={6}>Symptom Analyzer</Heading>
      <Textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Describe your symptoms..."
        size="lg"
        mb={4}
      />
      <Button colorScheme="blue" onClick={analyzeSymptoms}>
        Analyze
      </Button>
      
      {result && (
        <Box mt={8} p={4} borderWidth="1px" borderRadius="lg">
          <Heading size="md">Diagnosis: {result.condition}</Heading>
          <p>Confidence: {result.confidence}</p>
          <p>Recommendation: {result.recommendation}</p>
        </Box>
      )}
    </Box>
  );
}
