import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/Form.css"


// formulário genérico para login e registro
function Form({ route, method }) {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [loading, setLoading] = useState(false)
    const navigate = useNavigate()

    const name = method === 'login' ? "Login" : "Register"  // login ou register

    const handleSubmit = async (e) => { // processar o envio do formulário
        setLoading(true)  // Ativa indicador de carregamento
        e.preventDefault() // Impede reload da página

        try {
            const res = await api.post(route, { username, password }) // Faz uma requisição POST para a API. Envia os dados de username e password

            // Tratamento de Login/Registro
            if (method === 'login') { // Armazena tokens de acesso no localStorage
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh)
                navigate("/") // Redireciona para home (/)
            } else {
                navigate("/login") // Redireciona para página de login
            }
        } catch (error) { // Tratamento de Erros
            alert(error) // Captura e exibe qualquer erro que ocorra
        } finally {
            setLoading(false) // Desativa o estado de loading independentemente do resultado
        }
    }

    return <form onSubmit={handleSubmit} class="form-container"> 
        <h1>{name}</h1>  {/* login ou register */}
        
        <input // coletar o nome de usuário no formulário de login/registro
            className="form-input"
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)} // atualiza o estado username a cada digitação
            // O React controla o que é exibido. Cada mudança no campo username passa pelo estado do React
            placeholder="Username"
        />
        <input // coletar o nome de usuário no formulário de login/registro
            className="form-input"
            type="password" // Para o texto aparecer mascarado
            value={password}
            onChange={(e) => setPassword(e.target.value)} // atualiza o estado username a cada digitação
            // O React controla o que é exibido. Cada mudança no campo username passa pelo estado do React
            placeholder="Password"
        />
        <button className="form-button" type="submit">
            {name} {/* login ou register */}
        </button>

    </form>

}

export default Form // exporta a função!