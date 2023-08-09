import { Network } from "../types/network.type";

export const Networks: Network[] = [
    {
        network: "Bitcoin",
        symbol: "BTC",
        logo: "https://cryptoicons.org/api/icon/btc/200",
        endpoint: "btc-create"
    },
    {
        network: "Ethereum",
        symbol: "ETH",
        logo: "https://cryptoicons.org/api/icon/eth/200",
        endpoint: "eth-create"
    }
]