type TPayload = boolean | string;

export interface IAction {
	type: string,
	payload: TPayload,
}
