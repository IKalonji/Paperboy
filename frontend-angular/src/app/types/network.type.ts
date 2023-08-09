export interface Network {
    network: string,
    symbol: string,
    logo: string,
    endpoint: string
}

export interface GeneratorResponse {
    result: string,
    error?: string
    data?:any
}

export interface Keys {
    pubkey:string,
    privkey: string
}