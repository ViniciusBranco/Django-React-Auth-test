// Configuração de uma instância base do Axios para fazer requisições HTTP.
import axios from 'axios'; // biblioteca popular para fazer requisições HTTP (interceptador)
import { ACCESS_TOKEN } from './constants'; // constante importada do arquivo constants.js

const api = axios.create({ // instância configurada do Axios
    baseURL: import.meta.env.VITE_API_URL // URL base está configurada como "http://localhost:8000/"
})
// Agora só precisa especificar qual endpoint sem precisar repetir a URL base.
// exemplo: em vez de escrever:
// axios.get('http://localhost:8000/users')
// usamos:
// api.get('/users')

api.interceptors.request.use( // interceptador de requisições do Axios; será executado antes de cada requisição HTTP
    // Permite modificar ou validar a requisição antes que ela seja enviada ao servidor
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN) // Recupera o token de acesso do localStorage do navegador
        if (token) { // Se existir um token
            // Adiciona o header Authorization com o formato Bearer {token}
            config.headers.Authorization = `Bearer ${token}` // ste é um padrão comum em autenticação JWT (JSON Web Token)
        }
        return config // Retorna a configuração modificada
    },
    (error) => { // Função que lida com erros que podem ocorrer durante a interceptação
        return Promise.reject(error) // Rejeita a Promise com o erro original, permitindo que seja tratado posteriormente
        // Isso permite que o erro seja tratado posteriormente usando .catch()
    }
)

export default api // Exporta a instância configurada do Axios como padrão
// Permite que outros arquivos importem e utilizem esta configuração