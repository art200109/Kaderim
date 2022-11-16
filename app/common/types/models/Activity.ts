import { BaseModel } from '../BaseModel';
import { Rank, Location, Role } from '../enums';

export interface Activity extends BaseModel {
  name: string;
  description: string;
  startTime: Date;
  endTime: Date;
  requiredRanks?: Rank[];
  requiredRoles?: Role[];
  locations: Location[];
  soldiersNumber: number;
}
