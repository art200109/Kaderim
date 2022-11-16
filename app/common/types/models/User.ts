import { BaseModel } from '../BaseModel';
import { Gender } from '../enums';
import { Rank } from '../enums/Rank';
import { Role } from '../enums/Role';

export interface User extends BaseModel {
  name: string;
  gender: Gender;
  isAdmin: boolean;
  role: Role;
  rank: Rank;
  location: Location;
}
