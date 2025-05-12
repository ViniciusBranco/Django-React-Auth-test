// componente principal da aplicação React que gerencia o roteamento
// esta é uma aplicação web com sistema de autenticação, 
// onde algumas rotas só podem ser acessadas por usuários logados.

// componentes necessários do React e react-router-dom para gerenciamento de rotas
import React from 'react'
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom"

// paginas e logica da rota protegida
import Login from './pages/Login'
import Register from './pages/Register'
import Home from './pages/Home'
import NotFound from './pages/NotFound'
import ProtectedRoute from './components/ProtectedRoute'


function Logout() {
  localStorage.clear() // Limpa o localStorage (remove dados de autenticação)
  return <Navigate to="/login" /> // Redireciona o usuário para a página de login
}

function RegisterAndLogout() {
  localStorage.clear() // Limpa o localStorage (remove dados de autenticação)
  return <Register /> // Redireciona o usuário para a página de registro
}

// Componente Principal
function App() {

  return ( // gerenciar a navegação, estrutura de roteamento da aplicação
    <BrowserRouter> 
      <Routes>
        <Route // Página Home
          path="/"
          element={ // Rota protegida que renderiza o componente Home
            <ProtectedRoute>
              <Home /> 
            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} /> // Página de login
        <Route path="/logout" element={<Logout />} /> // Executa logout e redireciona para login
        <Route path="/register" element={<RegisterAndLogout />} /> // Página de registro
        <Route path="*" element={<NotFound />} /> // Rota padrão para páginas não encontradas
      </Routes>    
    </BrowserRouter>
  )
}

export default App
