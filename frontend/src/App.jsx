import { ChakraProvider } from '@chakra-ui/react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Diagnosis from './components/Diagnosis';
import Auth from './components/Auth';

export default function App() {
  return (
    <ChakraProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Diagnosis />} />
          <Route path="/auth" element={<Auth />} />
        </Routes>
      </BrowserRouter>
    </ChakraProvider>
  );
}
