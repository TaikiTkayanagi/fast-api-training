export interface Memo {
    id: number,
    title: string,
    content: string,
    status: Status
}

export interface Status {
    id: number,
    deadline?: Date,
    is_complete: boolean,
}

export interface Memos {
    memos: Memo[],
}