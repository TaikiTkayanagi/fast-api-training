export interface Memo {
    id: number,
    title: string,
    content: string,
}

export interface Memos {
    memos: Memo[],
}

export interface MemoForm {
    title: string,
    content: string,
}