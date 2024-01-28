// Cynhyrchwyd y ffeil hon yn awtomatig. PEIDIWCH Â MODIWL
// This file is automatically generated. DO NOT EDIT
import {context} from '../models';
import {httpfuncs} from '../models';

export function CancelQueue(arg1:number):Promise<void>;

export function CheckMasterPassword(arg1:string):Promise<boolean>;

export function GetDarkMode():Promise<boolean>;

export function GetName():Promise<string>;

export function Greet(arg1:string):Promise<string>;

export function NewDownloadQueue(arg1:context.Context,arg2:Array<httpfuncs.RequestArgs>):Promise<void>;

export function PromptMasterPassword():Promise<boolean>;

export function ResetEncryptedFields():Promise<void>;

export function SetDarkMode(arg1:boolean):Promise<void>;
