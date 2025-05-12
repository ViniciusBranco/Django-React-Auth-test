import { Navigate } from "react-router-dom"; // Para redirecionamento
import { jwtDecode } from "jwt-decode"; // Para decodificar tokens JWT
import api from "../api";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import { useState, useEffect} from "react"; // Hooks do React


function ProtectedRoute({children}) {
    
    // Estado do Componente, inicia isAuthorized como null, e usar a função setIsAuthorized para alterar o estado
    const [isAuthorized, setIsAuthorized] = useState(null);
    // useState null, true ou false:
    // null: estado inicial (loading)
    // true: usuário autenticado
    // false: usuário não autenticado

    useEffect(() => {
        auth().catch(() => setIsAuthorized(false))
    }, [])

    const refreshToken = async () => {
        // Atualiza o token de acesso usando o refresh token
        const refreshToken = localStorage.getItem(REFRESH_TOKEN);
        try {
            const res = await api.post("/api/token/refresh/", {refresh: refreshToken}); // Faz uma requisição POST
            if (res.status === 200) { // Salva o novo token no localStorage se bem sucedido
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                setIsAuthorized(true);
            }
        } catch (error) {
            console.log(error)
            setIsAuthorized(false)
        }

    }

    const auth = async () => {
        // checa se é preciso atualizar token ou continuar
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (!token) {
            setIsAuthorized(false);
            return;
        }
        const decode = jwtDecode(token);
        const tokenExpiration = decode.exp;
        const now = Date.now() / 1000; // data em segundos, não milissegundos

        if (tokenExpiration < now) {
            await refreshToken();
        } else {
            setIsAuthorized(true);
        }
        
    }

    if (isAuthorized === null) {
        return <div>Loading...</div>; // Mostra "Loading" durante a verificação
    } 
    // Renderiza o conteúdo protegido (children) se autenticado
    return isAuthorized ? children : <Navigate to="/login" />;
    // Redireciona para /login se não autenticado
}

export default ProtectedRoute;
